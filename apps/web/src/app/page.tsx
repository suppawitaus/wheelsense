export default function Home() {
  const api = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";
  return (
    <main>
      <h1>Wheelsense Web</h1>
      <p>Stack is running. API base: {api}</p>
      <p>Next steps: add SSE, devices, and readings.</p>
    </main>
  );
}
