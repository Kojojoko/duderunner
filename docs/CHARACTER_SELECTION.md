# 🏃 CHARACTER SELECTION ADDED!

## ✅ Feature Complete: Choose Your Hero

### What Was Added

**Single Player Character Selection Screen** where you can choose between:
- **AGAN (Hero)**: The classic green-shirt hero
- **KURAL (Mamitha)**: The new red-shirt heroine

---

## 🎮 How It Works

### Flow
1. **Main Menu** → Click "1 PLAYER"
2. **Character Select** → Choose "AGAN" or "KURAL"
3. **Difficulty Select** → Choose difficulty
4. **Game Start** → Play as your chosen character!

*Note: In 2-Player mode, characters are fixed (P1=Agan, P2=Kural).*

---

## 🔧 Technical Implementation

### Dynamic Animation System
To make this work, checking for `'run'` or `'jump'` animations is now dynamic:

```javascript
// Variable keys based on selection
let p1RunKey = 'run';         // or 'mamitha_run'
let p1JumpKey = 'jump';       // or 'mamitha_jump'
let p1DeathKey = 'death';     // or 'mamitha_death'

// In Update Loop
player.play(p1RunKey);

// In Jump Input
player.play(p1JumpKey);

// In Collision
player.play(p1DeathKey);
```

### Texture Swapping
When you select Kural, the main `player` sprite texture is swapped:
```javascript
player.setTexture('mamitha_sheet');
```
And reset to `'hero_sheet'` if you select Agan.

### State Management
- `selectedCharacter` variable tracks choice ('agan' or 'kural')
- State is **reset** when game restarts (Game Over -> Retry) so you can choose again.

---

## 🎨 UI Updates

**New Screen: SELECT CHARACTER**
- **AGAN Button**: Green theme
- **KURAL Button**: Orange/Red theme
- Includes hover effects and descriptions

---

## ✅ Verification Checklist

- ✅ Clicking "1 PLAYER" shows Character Select
- ✅ Clicking "AGAN" -> Sets Hero sprites
- ✅ Clicking "KURAL" -> Sets Mamitha sprites
- ✅ "2 PLAYER" mode skips this (Standard setup)
- ✅ Jump animations work for both
- ✅ Death animations work for both
- ✅ Game Over restart resets selection

---

## 🚀 Status

**CHARACTER SELECTION: READY!** 🎮

- Choose your hero!
- Play as Mamitha in single player!
- Full animation support!

**Run `play_game.bat` to test!**
