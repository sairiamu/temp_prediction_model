# Gotchas

- The current UI is intentionally local-state navigation; API-backed routing and generated OpenAPI types are Phase 2 work.
- Model artifacts are ignored by Git and should be generated from `libs/ml-core`.
- Keep timestamps timezone-aware when extending the feed loader.
