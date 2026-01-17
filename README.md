# FocusTokens

FocusTokens is a token-based attention and check-in system. Users receive daily tokens and spend them to send "pings" (normal or urgent). Tokens reset daily and all actions are recorded for history.

## Planned Features (MVP)
- Daily token balances with reset rules
- Send normal/urgent pings with costs
- Ping history
- Settings (daily tokens, costs)
- Persistence (SQLite)

## Development Plan
- Phase 1: Core logic + SQLite + CLI prototype
- Phase 2: Flask web UI reusing the same core services

## Project Structure
- `src/core` - business logic (tokens, pings)
- `src/data` - SQLite + repositories
- `src/cli` - CLI interface
- `src/web` - Flask web UI (later)
- `diagrams` - UML/DFD exports
- `tests` - unit/integration tests
