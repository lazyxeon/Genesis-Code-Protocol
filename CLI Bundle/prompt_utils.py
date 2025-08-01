import openai

def run_prompt(prompt):
    print("🧠 Engaging GPT for Phase 1...")
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are the Genesis Recursive Code Protocol assistant."},
            {"role": "user", "content": f"Begin GCP Phase 1 for: {prompt}"}
        ]
    )
    print("📨 GPT Response:")
    print(response['choices'][0]['message']['content'])
