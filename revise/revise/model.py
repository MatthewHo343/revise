import os

import cohere
import numpy as np

_DATA_DIRNAME = os.path.join(os.path.dirname(__file__), "prompt_data")

def get_feedback(history, text, co, model="xlarge"):
    """Gets feedback on text based on chat history."""
    
    history = f"\nuser: Here is what I have written so far: {text}\n" + history
    prompt_path = os.path.join(_DATA_DIRNAME, "get_feedback.prompt")
    with open(prompt_path) as f:
        prompt = f.read() + history + "\n-"

    prediction = co.generate(
        model=model,
        prompt=prompt,
        max_tokens=50,
        temperature=0.75,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["\n"],
        return_likelihoods="GENERATION",
        num_generations=4,
    )

    likelihood = [g.likelihood for g in prediction.generations]
    result = prediction.generations[np.argmax(likelihood)].text
    return result.strip()