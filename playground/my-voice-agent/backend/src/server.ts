import express, { Express, Request, Response, NextFunction } from 'express';
import cors, { CorsOptions } from 'cors';
import dotenv from 'dotenv';

// Load the .env file
dotenv.config();

// Create Express app
const app: Express = express();
const PORT: number = parseInt(process.env.PORT || '3001', 10);
const FRONTEND_URL: string = process.env.FRONTEND_URL || 'http://localhost:5173';
const OPENAI_API_KEY: string | undefined = process.env.OPENAI_API_KEY;

// Check if API key exists
if (!OPENAI_API_KEY) {
    console.error('❌ ERROR: OPENAI_API_KEY is not set in .env file');
    console.error('Please edit backend/.env and add your OpenAI API key');
    process.exit(1);
}

console.log('✅ OpenAI API key loaded successfully');

// Configure CORS to allow frontend access
const corsOptions: CorsOptions = {
    origin: FRONTEND_URL,
    credentials: true,
    methods: ['GET', 'POST'],
    allowedHeaders: ['Content-Type', 'Authorization']
};

// Apply middleware
app.use(cors(corsOptions));
app.use(express.json());

// Types for API responses
interface EphemeralKeyResponse {
    value: string;
    expires_at: number;
}

interface ErrorResponse {
    error: string;
    message?: string;
}

// Health check endpoint - to see if server is running
app.get('/health', (req: Request, res: Response): void => {
    res.json({
        status: 'ok',
        timestamp: new Date().toISOString(),
        message: 'Backend is running!'
    });
});

// Main endpoint - generates temporary keys for the frontend
app.post('/api/ephemeral-key', async (req: Request, res: Response<EphemeralKeyResponse | ErrorResponse>): Promise<void> => {
    try {
        console.log('📝 Generating new ephemeral key...');

        // Call OpenAI's API to get a temporary key
        const response: Response = await fetch('https://api.openai.com/v1/realtime/client_secrets', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${OPENAI_API_KEY}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                session: {
                    type: 'realtime',
                    model: 'gpt-realtime'
                }
            })
        });

        // Check if it worked
        if (!response.ok) {
            const errorText: string = await response.text();
            console.error('❌ OpenAI API error:', errorText);
            res.status(response.status).json({
                error: 'Failed to generate ephemeral key',
                message: errorText
            });
            return;
        }

        // Parse the response
        const data: EphemeralKeyResponse = await response.json();
        console.log('✅ Ephemeral key generated successfully');

        // Send key to frontend
        res.json({
            value: data.value,
            expires_at: data.expires_at || Date.now() + 60000
        });
    } catch (error) {
        console.error('❌ Error generating ephemeral key:', error);
        res.status(500).json({
            error: 'Internal server error',
            message: error instanceof Error ? error.message : 'Unknown error'
        });
    }
});

// Error handler
app.use((err: Error, req: Request, res: Response, next: NextFunction): void => {
    console.error('❌ Unhandled error:', err);
    res.status(500).json({
        error: 'Internal server error',
        message: err.message
    });
});

// Start the server
app.listen(PORT, (): void => {
    console.log('');
    console.log('🚀 Backend server is running!');
    console.log(`📍 URL: http://localhost:${PORT}`);
    console.log('');
    console.log('Available endpoints:');
    console.log(`  ✅ Health Check: http://localhost:${PORT}/health`);
    console.log(`  🔑 Get Key:      http://localhost:${PORT}/api/ephemeral-key`);
    console.log('');
    console.log('Waiting for frontend to connect...');
});