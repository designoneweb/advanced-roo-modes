## 🗂️ TASK DISPATCH LOOP  (MicroManager only)

**Ledger path**: `.roo/task-ledger.json`
**Context path**: `.roo/context.json`

### Algorithm
1. Load the ledger JSON.
2. For each task whose `status` is "TODO" **and** whose `deps`
   are all listed in `completed`, mark it "IN_PROGRESS", save
   the ledger, then delegate via `new_task` using:
     • mode        = task.mode
     • Context     = relevant slice of context.json
     • Scope/Focus = one‑line description
     • Outcome     = success criteria
3. When an `attempt_completion` callback arrives:
     • Update `status` → "DONE" or "FAILED"
     • Write summary into task.result
     • Push id into `completed` if DONE
     • If FAILED and retries >= 2, escalate by cloning task
       with next‑higher mode and appending it.
     • Save the ledger.
4. If every task in ledger.tasks is "DONE", produce a final
   user summary of results.
5. After the summary has been sent **and** no further tasks remain:

   • **Archive** – copy the full ledger to  
     `.roo/archive/ledger-$(date +%Y-%m-%dT%H%M%S).json`  
     (create the `archive/` folder if it doesn’t exist).

   • **Prune** – overwrite `.roo/task‑ledger.json` with a
     compact stub so future prompts stay small:

     ```json
     {
       "tasks": [
         {
           "id": "summary",
           "result": "All tasks completed ✅",
           "timestamp": "<ISO8601>"
         }
       ],
       "completed": [],
       "context": {}
     }
     ```

   • **Note** – call `set_ctx("notes", "Ledger archived → <timestamp>")`
     so other agents are aware.