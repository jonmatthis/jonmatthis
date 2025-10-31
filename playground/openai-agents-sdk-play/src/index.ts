import 'dotenv/config';
import { Agent, run } from '@openai/agents';

if (!process.env.OPENAI_API_KEY) {
  throw new Error('Missing OPENAI_API_KEY. Put it in .env or export it.');
}

// Agents
const historyTutorAgent = new Agent({
  name: 'History Tutor',
  instructions:
    'You provide assistance with historical queries. Explain important events and context clearly.',
});

const mathTutorAgent = new Agent({
  name: 'Math Tutor',
  instructions:
    'You provide help with math problems. Explain your reasoning at each step and include examples',
});

// Orchestrator
const triageAgent = new Agent({
  name: 'Triage Agent',
  instructions:
    "You determine which agent to use based on the user's homework question",
  handoffs: [historyTutorAgent, mathTutorAgent],
});

async function main() {
  const result = await run(triageAgent, 'What is the capital of France?');
  console.log('Final output:', result.finalOutput);
  console.log('Final agent:', JSON.stringify(result.rawResponses,null,2))
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});