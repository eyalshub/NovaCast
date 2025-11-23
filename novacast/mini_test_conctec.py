# mini_test_conctec.py
from app.services.llm.factory import create_language_model

llm = create_language_model("ollama", "phi:latest")
print(llm.generate_text("Tell me how beautiful Hadar is, my beloved Queen."))
