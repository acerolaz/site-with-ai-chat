"use client";

import { useRef, useState } from "react";
import { sendChat } from "@/lib/api";

type Message = { role: "user" | "assistant"; content: string };

export default function ChatPanel({ onMutation }: { onMutation?: () => void }) {
  const sessionId = useRef(crypto.randomUUID());
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSend(e: React.FormEvent) {
    e.preventDefault();
    if (!input.trim() || loading) return;
    const userMsg: Message = { role: "user", content: input };
    setMessages((m) => [...m, userMsg]);
    setInput("");
    setLoading(true);
    try {
      const { reply } = await sendChat(userMsg.content, sessionId.current);
      setMessages((m) => [...m, { role: "assistant", content: reply }]);
      onMutation?.();
    } catch (e) {
      setMessages((m) => [
        ...m,
        { role: "assistant", content: `Erreur : ${(e as Error).message}` },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="border rounded p-3 flex flex-col h-full">
      <h2 className="text-xl font-semibold mb-3">Chat IA</h2>
      <div className="flex-1 overflow-y-auto space-y-2 min-h-[300px]">
        {messages.length === 0 && (
          <p className="text-gray-500 text-sm">
            Demande-moi par exemple : « Quelles recettes j'ai ? » ou « Ajoute une tarte aux fraises ».
          </p>
        )}
        {messages.map((m, i) => (
          <div
            key={i}
            className={`p-2 rounded ${m.role === "user" ? "bg-blue-50 ml-8" : "bg-gray-50 mr-8"}`}
          >
            <div className="text-xs text-gray-500">
              {m.role === "user" ? "Toi" : "Assistant"}
            </div>
            <div className="whitespace-pre-wrap">{m.content}</div>
          </div>
        ))}
        {loading && <div className="text-sm text-gray-500">…</div>}
      </div>
      <form onSubmit={handleSend} className="mt-3 flex gap-2">
        <input
          className="border p-2 flex-1 rounded"
          placeholder="Écris un message…"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          disabled={loading}
        />
        <button
          className="bg-blue-600 text-white px-4 py-2 rounded disabled:opacity-50"
          disabled={loading}
        >
          Envoyer
        </button>
      </form>
    </div>
  );
}
