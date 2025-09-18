import './style.css';
import { RealtimeAgent, RealtimeSession } from '@openai/agents-realtime';

// Backend URL - this is where we'll get our keys from
const BACKEND_URL: string = 'http://localhost:3001';

// Get elements from the HTML
const statusDiv: HTMLDivElement = document.getElementById('status') as HTMLDivElement;
const connectBtn: HTMLButtonElement = document.getElementById('connect-btn') as HTMLButtonElement;
const conversationDiv: HTMLDivElement = document.getElementById('conversation') as HTMLDivElement;

// Track connection state and session
let isConnected: boolean = false;
let currentSession: RealtimeSession | null = null;

// Types for our API responses
interface EphemeralKeyResponse {
    value: string;
    expires_at: number;
}

// Create the AI agent
const agent: RealtimeAgent = new RealtimeAgent({
    name: 'Assistant',
    instructions: 'You are a helpful and friendly assistant. Be concise and clear.',
});

// Function to create and set up a new session
function createSession(): RealtimeSession {
    const session: RealtimeSession = new RealtimeSession(agent, {
        model: 'gpt-realtime',
    });

    // Listen for when we connect
    session.on('connected', (): void => {
        isConnected = true;
        statusDiv.textContent = '🟢 Connected! Start speaking...';
        statusDiv.className = 'connected';
        addMessage('System', '✅ Connected! You can start talking now.');
        connectBtn.textContent = 'Disconnect';
        connectBtn.disabled = false;
    });

    // Listen for when we disconnect
    session.on('disconnected', (): void => {
        isConnected = false;
        statusDiv.textContent = 'Disconnected';
        statusDiv.className = '';
        connectBtn.textContent = 'Connect to Agent';
        connectBtn.disabled = false;
        addMessage('System', '🔌 Disconnected from voice agent.');
    });

    // Listen for errors
    session.on('error', (error: any): void => {
        statusDiv.textContent = `❌ Error: ${error.message || error.toString()}`;
        statusDiv.className = 'error';
        console.error('Session error:', error);
        isConnected = false;
        connectBtn.textContent = 'Connect to Agent';
        connectBtn.disabled = false;
    });

    // Listen for conversation updates
    session.on('conversation.updated', (event: any): void => {
        console.log('Conversation updated:', event);
        if (event?.item?.role === 'assistant' && event?.item?.formatted?.transcript) {
            addMessage('Assistant', event.item.formatted.transcript);
        }
        if (event?.item?.role === 'user' && event?.item?.formatted?.transcript) {
            addMessage('You', event.item.formatted.transcript);
        }
    });

    // Additional useful events
    session.on('response.audio.started', (): void => {
        console.log('🔊 Assistant started speaking');
    });

    session.on('response.audio.done', (): void => {
        console.log('🔇 Assistant finished speaking');
    });

    session.on('input_audio_buffer.speech_started', (): void => {
        console.log('🎤 User started speaking');
    });

    session.on('input_audio_buffer.speech_stopped', (): void => {
        console.log('🤐 User stopped speaking');
    });

    return session;
}

// Function to add messages to the conversation box
function addMessage(speaker: string, text: string): void {
    const messageDiv: HTMLDivElement = document.createElement('div');
    messageDiv.className = 'message';
    const time: string = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    messageDiv.innerHTML = `<strong>${speaker} (${time}):</strong> ${text}`;
    conversationDiv.appendChild(messageDiv);
    conversationDiv.scrollTop = conversationDiv.scrollHeight;
}

// Function to get a temporary key from our backend
async function getEphemeralKey(): Promise<string> {
    try {
        const response: Response = await fetch(`${BACKEND_URL}/api/ephemeral-key`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.statusText}`);
        }

        const data: EphemeralKeyResponse = await response.json();
        console.log('Got ephemeral key, expires at:', new Date(data.expires_at).toLocaleTimeString());
        return data.value;
    } catch (error) {
        console.error('Error getting key:', error);
        throw error;
    }
}

// Function to disconnect current session
async function disconnectSession(): Promise<void> {
    if (currentSession) {
        try {
            // Try different methods based on what's available
            if ('close' in currentSession && typeof currentSession.close === 'function') {
                await (currentSession as any).close();
            } else if ('stop' in currentSession && typeof currentSession.stop === 'function') {
                await (currentSession as any).stop();
            } else if ('end' in currentSession && typeof currentSession.end === 'function') {
                await (currentSession as any).end();
            } else {
                // If no disconnect method exists, just reset our state
                console.log('No disconnect method found, resetting state');
            }
        } catch (error) {
            console.error('Error during disconnect:', error);
        }

        // Clean up
        currentSession = null;
        isConnected = false;
        statusDiv.textContent = 'Disconnected';
        statusDiv.className = '';
        connectBtn.textContent = 'Connect to Agent';
        connectBtn.disabled = false;
        addMessage('System', '🔌 Disconnected from voice agent.');
    }
}

// What happens when you click the connect button
connectBtn.addEventListener('click', async (): Promise<void> => {
    try {
        // If already connected, disconnect
        if (isConnected) {
            await disconnectSession();
            return;
        }

        // Disable button and update UI
        connectBtn.disabled = true;
        connectBtn.textContent = '🔑 Getting key...';
        statusDiv.textContent = 'Getting temporary key...';
        statusDiv.className = '';

        // Get a fresh key from our backend
        const ephemeralKey: string = await getEphemeralKey();

        // Update UI
        connectBtn.textContent = '🔌 Connecting...';
        statusDiv.textContent = 'Connecting to OpenAI...';

        // Create new session and connect
        currentSession = createSession();
        await currentSession.connect({ apiKey: ephemeralKey });

    } catch (error) {
        statusDiv.textContent = `❌ Failed: ${(error as Error).message}`;
        statusDiv.className = 'error';
        connectBtn.textContent = 'Connect to Agent';
        connectBtn.disabled = false;
        console.error('Connection error:', error);

        // Clean up on error
        currentSession = null;
        isConnected = false;
    }
});

// Check if backend is running when page loads
async function checkBackend(): Promise<void> {
    try {
        const response: Response = await fetch(`${BACKEND_URL}/health`);
        if (response.ok) {
            console.log('✅ Backend is running');
            connectBtn.disabled = false;
            statusDiv.textContent = '✅ Ready to connect';
        } else {
            throw new Error('Backend check failed');
        }
    } catch (error) {
        console.error('❌ Backend not available:', error);
        statusDiv.textContent = '❌ Backend not running. Please start the backend first!';
        statusDiv.className = 'error';
        connectBtn.disabled = true;
    }
}

// Check backend when page loads
window.addEventListener('load', (): void => {
    checkBackend();
});

// Clean up on page unload
window.addEventListener('beforeunload', (): void => {
    if (currentSession && isConnected) {
        disconnectSession();
    }
});