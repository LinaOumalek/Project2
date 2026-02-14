## 📅 Week X – Backend Fundamentals & API Design

### ✅ Outcomes

---

### 🖥️ Command Line (Linux/Terminal)

- Navigating the file system:
  - `pwd`, `cd`, `ls` (`-l`, `-a`)

- Manipulating files and directories:
  - `mkdir`, `mv`, `cp`, `touch`, `rm`, `rm -r`, `file`, `ln`

- Working with commands:
  - `man`, `whatis`, `type`, `alias`

- Input/Output Redirection

- Pipelines:
  - `sort`, `uniq`, `grep`, `head`, `tail`, `tee`

- Expansions and quoting:
  - `echo`, quoting rules

---

### 🌱 Version Control

- Basic version control workflow (Git)

---

### 🌐 API Endpoint Design (FastAPI + PostgreSQL)

#### 1️⃣ Layered Approach for Clean Endpoint Design

- **Input Validation (Pydantic Models)**
  - Type validation
  - Required fields
  - Optional constraints

- **Business Logic Validation (Inside Endpoints)**
  - Checking sufficient funds
  - Handling database constraints
  - Custom error handling

- **DB Constraints in db level**

---

#### 2️⃣ Structured API Responses

**Error Responses**

if amount <= 0:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="message"
    )

**Success Responses**

return {
    "status": "success",
    "data": {
        "account_id": account_id,
        "balance": new_balance,
        "withdrawn": amount,
        "currency": currency
    }
}