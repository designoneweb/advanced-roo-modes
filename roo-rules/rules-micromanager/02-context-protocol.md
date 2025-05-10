## 📦 CONTEXT STORE PROTOCOL  (MicroManager only)

**File path**: `.roo/context.json`

### Helper Behaviours
1. **get_ctx(key)** – open the JSON, parse, return ctx[key] (or "" if absent).
2. **set_ctx(key, value)** – read → modify ctx[key] = value → save JSON.
3. **Standard keys**
   • "plan"               – Architect’s full design doc  
   • "stack_docs"         – map: tech‑stack element → info  
   • "latest_test_result" – Tester JSON from last run  
   • "notes"              – free‑form inter‑agent notes
4. Always write *valid* JSON; never leave the file half‑written.
5. Use these helpers whenever you delegate tasks or need shared info.