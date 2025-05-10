## Ledger Protocol  (internal – for MicroManager only)

*Ledger Location*: `.roo/task-ledger.json`

### Task Object Shape
```json
{
  "id": "uuid",
  "description": "human text",
  "mode": "junior",
  "deps": ["uuid1", "uuid2"],
  "status": "TODO | IN_PROGRESS | DONE | FAILED",
  "retries": 0,
  "result": ""
}
