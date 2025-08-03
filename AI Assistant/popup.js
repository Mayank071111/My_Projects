const geminiApiKey = "AIzaSyA6pA6Y5RPZ2-CbU30KAvpZaZWOGtwZC3U";  // Store securely!
const inputField = document.getElementById("inputText");
const outputField = document.getElementById("output");
const grammarButton = document.getElementById("checkGrammar");
const replyButton = document.getElementById("suggestReply");

// Grammar Check using LanguageTool API (Free)
grammarButton.addEventListener("click", async () => {
    const text = inputField.value.trim();
    if (!text) {
        outputField.innerText = "⚠️ Please enter some text first!";
        return;
    }
    outputField.innerText = "⏳ Checking grammar...";
    const corrected = await grammarCheck(text);
    outputField.innerText = corrected;
});

// Reply Suggestion using Google Gemini API (Free)
replyButton.addEventListener("click", async () => {
    const text = inputField.value.trim();
    if (!text) {
        outputField.innerText = "⚠️ Please enter text first!";
        return;
    }
    outputField.innerText = "⏳ Generating reply suggestion...";
    const reply = await suggestReply(text);
    outputField.innerText = reply;
});

// Grammar Correction (LanguageTool)
async function grammarCheck(text) {
    const response = await fetch("https://api.languagetool.org/v2/check", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ language: "en-US", text })
    });

    const data = await response.json();

    if (data.matches.length === 0) return "✔ Grammar and spelling look good!";

    // Build suggestions with corrected words
    return data.matches
        .map(m => {
            const suggestion = m.replacements.length > 0 ? 
                `→ Suggestion: ${m.replacements[0].value}` : 
                "(No suggestion available)";
            return `• ${m.message}\n${suggestion}`;
        })
        .join("\n\n");
}


// async function grammarCheck(text) {
//     const response = await fetch("https://api.languagetool.org/v2/check", {
//         method: "POST",
//         headers: { "Content-Type": "application/x-www-form-urlencoded" },
//         body: new URLSearchParams({ language: "en-US", text })
//     });
//     const data = await response.json();
//     if (data.matches.length === 0) return "✅ Grammar looks good!";
//     return data.matches.map(m => `✏️ ${m.message}`).join("\n");
// }

// Reply Suggestion (Gemini)
async function suggestReply(text) {
    const prompt = `Read this message and suggest a short, polite reply:\n\n${text}`;
    return await callGeminiAPI(prompt);
}

// Google Gemini API Call
async function callGeminiAPI(prompt) {
    try {
        const res = await fetch(
            `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${geminiApiKey}`,
            {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    contents: [{ role: "user", parts: [{ text: prompt }] }]
                })
            }
        );

        if (!res.ok) {
            const error = await res.text();
            console.error("Gemini API Error:", error);
            return "❌ Gemini API Error (check console)";
        }

        const data = await res.json();
        return data.candidates?.[0]?.content?.parts?.[0]?.text || "⚠️ No reply generated.";
    } catch (err) {
        console.error("Fetch Error:", err);
        return "❌ Failed to connect to Gemini API.";
    }
}
