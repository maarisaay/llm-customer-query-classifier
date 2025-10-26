# Architecture & Technical Plan (Azure + Databricks)

## 1) Ingestion / Feature Store 
- **Text hygiene & PII**: usunięcie znaczników HTML, podpisów i cytatów, deduplikacja (hashowanie), anonimizacja danych osobowych (adresy e-mail, numery telefonów, identyfikatory użytkowników)
- **Enrichment & language**: wykrywanie języka, analiza sentymentu i długości wiadomości, dodanie metadanych - kanał (email/chat), źródło, produkt, segment użytkownika, znacznik czasu
- **Representation for modeling**: generowanie wektorowych reprezentacji tekstu (np. przy użyciu `sentence-transformers/all-MiniLM-L6-v2` lub Azure `text-embedding-3-*`), przypisanie etykiet z historycznych danych routingu, zapisanie do Databricks Feature Store

## 2) Architektura LLM
### a) Gotowe API LLM (Azure OpenAI) – Prompt Engineering
- **System prompt** - zdefiniowanie roli modelu i schematu JSON jako jedynego dozwolonego formatu odpowiedzi, `temperature=0`, ograniczenie liczby tokenów
- **Few-shot learning** - dodanie 2-3 przykładów dla każdej klasy (w tym przypadków brzegowych)
- **Wymuszanie schematu** - użycie JSON Schema lub `function calling`, zastosowanie klasy zapasowej `OTHER` przy niskiej pewności klasyfikacji
- **Kontrola kosztów** - wcześniejsze przycinanie treści (usuwanie stopki, cytatów), krótkie prompty, batchowanie zapytań mailowych
- **Przykładowy output**:
  ```json {"labels":["billing_issue"], "confidence":0.82, "route":"L2_finance"}```

## 3) Wdrożenie produkcyjne
- **Serving**: Azure Functions / Databricks Model Serving za API Management (throttling, quota, OAuth2)
- **Skalowanie**: autoscaling Functions/AKS, batching, cache embeddings (Redis/Delta cache)
- **Bezpieczeństwo**: private link do Azure OpenAI/Cognitive Search, Managed Identity, Key Vault, RBAC (Unity Catalog), TLS, IP allowlist

