// app/page.tsx (Next.js App Router com Tailwind)
"use client";

import { useState, useRef, useEffect } from "react";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState<{ type: "user" | "bot"; text: string }[]>([]);
  const [loading, setLoading] = useState(false);
  const endRef = useRef<HTMLDivElement | null>(null);

  const scrollToBottom = () => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  const handleSend = async () => {
    if (!question.trim()) return;

    setMessages((prev) => [...prev, { type: "user", text: question }]);
    setLoading(true);

    try {
      const res = await fetch("http://localhost:5000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      const data = await res.json();
      setMessages((prev) => [...prev, { type: "bot", text: data.answer || "Erro na resposta." }]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [...prev, { type: "bot", text: "Erro ao se comunicar com a API." }]);
    } finally {
      setLoading(false);
      setQuestion("");
    }
  };

  return (
    <main className="max-w-2xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-4">Chat com RAG 🤖</h1>
      <div className="border rounded p-4 h-96 overflow-y-auto bg-gray-50 space-y-2">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`p-2 rounded-lg max-w-xs ${
              msg.type === "user"
                ? "bg-blue-600 text-white ml-auto"
                : "bg-gray-200 text-black"
            }`}
          >
            {msg.text}
          </div>
        ))}
        {loading && <div className="text-gray-500">Pensando...</div>}
        <div ref={endRef} />
      </div>
      <div className="flex mt-4">
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          className="flex-1 border px-4 py-2 rounded-l"
          placeholder="Digite sua pergunta..."
        />
        <button
          onClick={handleSend}
          className="bg-blue-600 text-white px-4 py-2 rounded-r hover:bg-blue-700"
        >
          Enviar
        </button>
      </div>
    </main>
  );
}
