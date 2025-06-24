# 🧪 Rogue Alchemy — Core Design

A roguelike focused on exploration, card crafting, and progression through discovery. The player navigates procedurally generated environments to collect materials while using a lab (or magical workshop) to create and upgrade their deck during and between runs.

---

## 🧱 1. Game Foundations

### The Player as a Character
- The player is not an abstract presence but a **character within the world**.
- They act as the **main alchemist**, directing expeditions, researching recipes, and making strategic decisions.
- **Heroes are companions**, represented by cards selected for each run.
- The player can have their own progression system: talents, passive skills, reputation, and world-affecting effects.
- This supports narrative depth and potential future multiplayer expansion.

- **Genre:** Roguelike + deckbuilding.
- **Play style:** Initially single-player, with cycles of exploration and creation.
- **Target platform:** Web and mobile (no complex animations).
- **Player goal:** Build the most powerful deck via expeditions and alchemy, unlocking new cards and materials each run.

## 🧭 2. Core Gameplay Loop

1. **Start of run:** The player selects a basic deck and a "focus recipe" (a card they aim to unlock).
2. **Procedural exploration:**
   - Randomly generated zones (dungeons, forests, ruins).
   - Encounters with enemies, traps, narrative events.
   - Battles using cards.
3. **Laboratory (interlude or end phase):**
   - Use materials to craft or upgrade cards.
   - Save progress on discovered recipes.
4. **Meta-progression:**
   - Unlock more materials, base cards, and permanent abilities.

## 🗺️ 2b. Map and Exploration

- Each run’s map is a **node network** (like Slay the Spire).
- Nodes include: battle, event, resource gathering, shop, temporary lab.
- The player chooses a route, affecting encounters and rewards.
- Maps vary based on zone/biome and are procedurally generated.
- Some paths require special conditions (relics, hero traits, cards).
- Exploration impacts material gathering and deck-building opportunities.

## ⚔️ 3. Card-Based Combat System

- Combat is **automatic**, based on the player’s prebuilt deck.
- The player forms a **team of heroes**, each represented by a card with stats and unique synergies.
- The player **does not play cards in combat**; instead, strategy lies in preparing the deck.
- The engine resolves combat using internal logic: card type, order, synergy.
- Card types include:
  - Attack (direct, AoE)
  - Defense (block, evade)
  - Alchemy (buffs, debuffs, modifiers)
- Cards can be upgraded, combined, or evolved in the lab.
- Enemies include bosses, elites, and regulars with unique patterns.
- Combat outcomes depend on deck quality, hero synergy, and preparation.
- Defeated enemies may drop new cards, materials, or temporary effects.

## 🔬 4. Alchemy & Crafting

- **Materials:** powders, essences, fragments, elemental ingredients.
- **Hidden recipes:**
  - Players discover new cards by mixing materials.
  - Some are linked to events or relics.
- **Upgrade system:**
  - Add effects, reduce costs, increase power, change type.

## 🧠 5. Player Classes

- Players choose a **character class** (unlockable over time).
- Each class shapes gameplay, card effectiveness, and hero synergy.

### Sample classes:

| Class       | Role               | Effects                                                   |
|-------------|--------------------|------------------------------------------------------------|
| Alchemist   | Versatile/support  | Faster recipe discovery, better crafting.                 |
| Warrior     | Aggressive         | Stronger battle heroes, bonus to attack cards.            |
| Mage        | Magic control      | Synergy with spells and complex card effects.             |
| Thief       | Exploration/loot   | Reveals hidden nodes, rare item boost.                   |
| Sage        | Knowledge path     | Faster XP gain, early access to rare recipes.             |

- Classes could have talent trees, impact narrative decisions, and unlock new zones.

## 🧠 6. Progression & Replayability

### a) Leveling and progression

- **Hero leveling:** heroes gain XP and unlock passive abilities and upgrades.
- **Card evolution:** cards gain XP and can be upgraded for improved effects.
- **Player progression:** unlocks heroes, recipes, zones, and lab upgrades.
- **Hero specialization:** develop into branches (offense, alchemy, support).

- **Run-based:** each attempt is different.
- **Persistent progress:**
  - Discovered recipes are saved.
  - Permanent unlocks (lab, characters, slots).
- **Increasing difficulty:** new mechanics, conditions, and zones over time.

## 🌍 7. Game Expansion

- The base game is expandable with modular content and systems.

### a) World and Zone Exploration

- New **zones**: cities, dungeons, forests, deserts, etc.
- Some are **permanent**, others tied to **events**.
- Zones have **difficulty levels**, materials, enemies, and unique NPCs.
- Incentivize exploration with rare materials and special challenges.

## 🧩 8. Gameplay Mechanics

### a) Zone Exploration
- Node-based procedural maps.
- Encounters: combat, events, NPCs, treasure/resource discovery.

### b) Laboratory
- Research recipes, create new cards, upgrade or modify existing ones.

### c) Expedition Preparation
- Choose heroes, build deck, assign initial equipment, review zone traits.
- Strategic planning phase.

### d) Ruin Exploration
- Sub-dungeons with interconnected rooms.
- Includes traps, mini-bosses, and high-risk/high-reward mechanics.

### e) Additional Activities
- Alchemy mini-games.
- Daily/weekly quests.
- Collection and deck management.
- NPC interactions and recipe hints.

## 🔗 9. Blockchain Integration (Optional)

- Optional Web3 layer. Default gameplay is Web2.

### How it works:

- Traditional: progress and cards saved locally or in backend.
- Wallet-connected: players can **tokenize assets** (cards, relics, recipes).
- Tokenized assets become NFTs:
  - Can be used, traded, rented.
  - Tokenization is manual and optional.

### Security and Balance
- NFTs offer no unfair advantage.
- Only certain assets qualify for tokenization (rarity, achievements).

## 📚 Other Ideas & Concepts

- Base-building systems.
- Rogue-lite loops.
- Card collection with progression.
- Rare combinations:
  - Fog of war
  - Crafting cards
  - Asynchronous PvP
  - Shared player decks
  - Procedural narrative decisions

## 💡 Concept Variants

### 1. "Wandering Refuge"
- Moving base over procedural map.
- Resource management, evolving characters.
- PvP base encounters.

### 2. "Paper Dungeon"
- Card-based roguelike dungeon.
- Room-by-room procedural layout.

### 3. "Ruins of Legacy"
- Base-building over ancient ruins.
- Each building unlocks cards.

### 4. "Rogue Alchemy"
- Core idea: procedural exploration, crafting via alchemy, auto-battles, persistent upgrades, future multiplayer potential.

