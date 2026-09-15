# README Audit Table

| Claim made in README | True? | Evidence or correction made |
| :--- | :---: | :--- |
| Requires `pip install -r requirements.txt` | No | No `requirements.txt` exists; standard library only. Delete the line. |
| Repository title is `Python-basics-25BCON1802` | Yes | Verified from GitHub repository page title and URL. |
| Contains `dictionary.py` | Yes | Verified file exists in repository root folder. |
| Contains `factorial.py` | Yes | Verified file exists in repository root folder. |
| Contains `fibonacci.py` | Yes | Verified file exists in repository root folder. |
| Requires Python 3.x | Yes | All `.py` scripts use Python 3 standard syntax. |
| Commands run directly via `python <script_name>.py` | Yes | No external dependencies or build steps needed. |
## Peer Review Notes 
I shared my repo with CHHAVI AGARWAL and she provided verified two claims and essential fixes 
### 2. Verify two claims

| Claim | True? | Evidence / Correction |
|---|---|---|
| `factorial.py` computes factorial of a user-specified number | No | The program currently sets `n = 5`, so it is not user-specified. :contentReference[oaicite:2]{index=2} |
| README lists `list.py`, `multiplication.py`, and `pattern.py` as included programs | No | These files are listed in README, but they are not present in the current repository root shown on GitHub. :contentReference[oaicite:3]{index=3} |

### 3. Commit messages
The commits are simple and suitable for a beginner repository. Keep using short, clear imperative commit messages such as:
- `feat: add pattern program`
- `feat: add list program`

### 4. One specific fix
Update the README so that the "Programs Included" section exactly matches the files currently present in the repository. Also change the factorial description from "user-specified number" to "calculates the factorial of 5", unless the code is changed to accept user input. :contentReference[oaicite:4]{index=4}
## Commit-message comparison

| Commit | My message | AI message | Which is clearer, and why? |
| :---: | :--- | :--- | :--- |
| 1 | `feat : add factorial program` | `feat: implement factorial calculation script` | **AI message** — Uses standard conventional commit formatting (no spaces before colon) and specifies the function instead of a generic "program". |
| 2 | `feat : fibonacci program` | `feat: add fibonacci sequence generator` | **AI message** — Fixes missing action verb and formatting while clearly stating what the script generates. |
| 3 | `feat : add dictionary program` | `feat: add dictionary key-value operations script` | **AI message** — Provides precise context about what aspects of dictionaries are being handled. |
| 4 | `feat : add multiplication program` | `feat: add multiplication table generator script` | **AI message** — Clarifies the exact functionality (table generation vs simple arithmetic). |
| 5 | `feat : add pattern program` | `feat: add star and number pattern printing script` | **AI message** — Clearly describes what kind of patterns the program renders. |
| 6 | `feat : add list program` | `feat: implement basic list operations and iteration` | **AI message** — Describes the actual data structure operations covered rather than using a vague title. |
