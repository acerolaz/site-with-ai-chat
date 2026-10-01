const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export type Recipe = {
  id: number;
  name: string;
  ingredients: string[];
};

export async function listRecipes(): Promise<Recipe[]> {
  const res = await fetch(`${API_URL}/recipes`, { cache: "no-store" });
  if (!res.ok) throw new Error("Échec liste recettes");
  return res.json();
}

export async function createRecipe(name: string, ingredients: string[]): Promise<Recipe> {
  const res = await fetch(`${API_URL}/recipes`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, ingredients }),
  });
  if (!res.ok) throw new Error("Échec création recette");
  return res.json();
}

export async function deleteRecipe(id: number): Promise<void> {
  const res = await fetch(`${API_URL}/recipes/${id}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Échec suppression");
}

export async function sendChat(message: string, sessionId: string): Promise<{ reply: string }> {
  const res = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, session_id: sessionId }),
  });
  if (!res.ok) throw new Error("Échec chat");
  return res.json();
}
