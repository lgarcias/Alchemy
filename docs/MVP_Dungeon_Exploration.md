[⬅️ Back to Project README](../README.md)

## 🎯 MVP - Rogue Alchemy: Dungeon Exploration

This document defines the scope of the **Minimum Viable Product (MVP)** for *Rogue Alchemy*, focused on a single-player game mode that allows:

- Creating a playable character.
- Exploring a **procedurally generated dungeon**.
- Participating in simplified tactical combat within the dungeon.

---

### 🧱 1. MVP Objective

- To have a functional prototype, playable on Android mobile (native export, with touch controls as a priority) and later on PC (browser), that validates exploration, combat flow, and character management.

---

### 🧪 2. Included Mechanics

#### A. Character Creation

- Name selection.
- Class selection (initially 2: **Alchemist** or **Warrior**).
- Generation of base stats (fixed or semi-random).
- Selection of initial abilities (simple passives or bonuses).

#### B. Procedural Dungeon

- Dungeon map composed of **rooms connected by doors**, procedurally generated on a **tile grid**.
- Player movement is **tile-by-tile** in a top-down view.
- Each room contains an event:
  - Combat (basic level random enemy).
  - Chest (random reward).
  - Healing or altar (1 in every 4 runs).
- Exploration interface similar to tile-based dungeon crawlers.

#### C. Turn-Based Tactical Combat

- Combat occurs on a tile grid, inside the dungeon rooms.
- Turn-based system where the player can:
  - Move across tiles.
  - Attack or use abilities based on class and equipment.
  - Use items if available.
- Enemies have simple movement and attack patterns.
- Each character has basic stats (HP, damage, defense, speed).
- Each class has one passive and one active ability.
- No cards are used in this initial version.
- Combat outcomes depend on the player’s turn decisions and preparation.

#### D. Progress System

- At the end of a dungeon:
  - Save character and stats (progress is only saved at dungeon completion).
  - Register gathered materials.
  - Show result summary.

---

### ⚙️ 3. Technical Requirements

- Compatible with HTML5 (playable in browser on mobile and PC).
- Exportable to Android as a native app (touch controls prioritized).
- Responsive interface.
- Minimal backend implemented with **FastAPI**:
  - User, character, and progress management.
  - Communication via REST API.
  - Connection to a **PostgreSQL** database for persistence.
- Local storage only as fallback.
- Uses Godot 4.2+ as game engine.

---

### 📌 4. Scope and Exclusions

#### Included:

- Playable character and randomly generated dungeon.
- Tile-based dungeon exploration.
- Basic turn-based tactical combat system.
- Simple game loop: start → exploration → result.
- Export to web and Android mobile.
- FastAPI backend connected to PostgreSQL.

#### Not included in this phase:

- Laboratory or card crafting system.
- Hero companions system.
- Advanced combat mechanics.
- Blockchain integration.

---

### ✅ 5. Validation Objectives

- Is exploration with basic combat fun and meaningful?
- Does the procedural dungeon format work with minimal resources?
- Does the player perceive progression between runs?
- Is the technical-functional architecture valid for future expansion?
- Is the mobile experience with touch controls fluid and intuitive?

---

### 🌐 6. MVP Deployment Note

- The MVP should be published on an accessible URL for external feedback and testing.
- **Deployment options:**
  - **Web version:**
    - Use Godot's HTML5 export and host on platforms like itch.io, Netlify, Vercel, or GitHub Pages.
    - Itch.io is popular for indie games and allows easy uploads and feedback.
    - Netlify/Vercel are good for static hosting and custom domains.
  - **Android version:**
    - Distribute the APK directly for testers or use Google Play (requires developer account and review process).
    - For closed tests, Google Play's internal testing or platforms like TestFairy can be used.

---

### 🛠️ 7. Minimum Task List

#### A. General Design

- ✅ Define character data structure (name, class, stats, abilities).
- ⏳ Define base classes: Alchemist and Warrior.
- [ ] Design connected room system and random content.
- [ ] Establish turn-based tactical combat mechanics (actions, turns, simple AI).
- ⏳ Define backend structure: entities, API routes, progress persistence.

#### B. Frontend Godot

- [ ] Create main menu scene and character selector.
- [ ] Implement dungeon exploration scene in top-down view using `TileMap`.
- [ ] Create procedural generation system for connected rooms.
- [ ] Implement tile-by-tile player movement.
- [ ] Detect room events (combat, chest, healing).
- [ ] Create turn-based tactical combat system:
  - [ ] Turn control.
  - [ ] Character movement on grid.
  - [ ] Actions: attack, ability, use item.
- [ ] Basic responsive UI for mobile and desktop.
- [ ] Save/load from JSON or localStorage (offline mode).

#### C. Backend FastAPI

- ⏳ Create models for user, character, and progress in SQLAlchemy.  
- ✅ Create API routes:
  - [ ] Registration and login.
  - ✅ Save/load characters (CRUD endpoints complete & tested).
  - [ ] Log explorations and progress.
- [ ] Connect to PostgreSQL database.
- [ ] Test communication with Godot client via `HTTPRequest`.
- [ ] Add automated tests for all character endpoints.

#### D. Integration

- [ ] Connect Godot to REST API (FastAPI) to retrieve and save data.
- [ ] Implement basic connection check and fallback to localStorage.
- [ ] Browser functionality tests.
- [ ] Export and test Android version.

#### E. Final Testing

- [ ] Validate character creation and persistence (API fully tested).
- [ ] Validate full dungeon exploration with procedural generation.
- [ ] Validate functional and balanced tactical combat.
- [ ] Check mobile compatibility (browser and app).
- [ ] Verify backend connection and remote saving.

