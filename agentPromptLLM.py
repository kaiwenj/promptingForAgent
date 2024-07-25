

class PromptGPT(object):

    def __init__(self, client, model):
        self.client=client
        self.model=model

    def __call__(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content
        return answer