# 📱 How to Build an APK for Dude Runner

Since this is an HTML5 game, you cannot "save as APK" directly. You need to use a wrapper tool. The easiest modern tool is **CapacitorJS**.

Here is a step-by-step guide to turning your game into an Android App (APK).

---

## 🛠️ Method 1: Website 2 APK (Easiest, No Coding)

If you don't want to install coding tools, use a "Web to App" converter.

1. **Host your game** on GitHub Pages or Netlify (so you have a URL like `https://mygame.netlify.app`).
2. Download **[Website 2 APK Builder](https://website2apk.com/)** (or similar tool).
3. Enter your game URL or select "Local HTML".
4. Choose your `index.html` folder.
5. Click **Build APK**.

---

## 👨‍💻 Method 2: CapacitorJS (Professional Way)

This method gives you a real native project that you can publish to the Play Store.

### Prerequisites
1. **Node.js** installed.
2. **Android Studio** installed (for building the final APK).

### Steps

#### 1. Optimization for Build
I have already updated your `index.html` with:
- ✅ **Touch Controls**: On-screen jump zones.
- ✅ **Pause Button**: Since phones don't have ESC.
- ✅ **Mobile Viewport**: Stops zooming/scrolling.
- ✅ **Manifest**: `manifest.json` added.

#### 2. Initialize Project
Open a terminal in your project folder (`duderunner`) and run:

```bash
# 1. Initialize a new Node project
npm init -y

# 2. Install Capacitor
npm install @capacitor/core @capacitor/cli @capacitor/android
npx cap init
#  - Name: Dude Runner
#  - Package ID: com.myname.duderunner
```

#### 3. Configure Capacitor
Edit `capacitor.config.json`:
```json
{
  "appId": "com.myname.duderunner",
  "appName": "Dude Runner",
  "webDir": ".", 
  "bundledWebRuntime": false
}
```
*Note: `webDir` should be "." if your index.html is in the root, or "www" if you move files there.*

#### 4. Build Android Project
```bash
# Add Android platform
npx cap add android

# Sync your web files to the native project
npx cap sync
```

#### 5. Generate APK
```bash
# Open Android Studio
npx cap open android
```
- In Android Studio, wait for Gradle sync.
- Go to **Build** > **Build Bundle(s) / APK(s)** > **Build APK**.
- Locate the APK in `android/app/build/outputs/apk/debug/app-debug.apk`.

---

## 🎮 Mobile Controls

I have updated the game to support touch automatically!

- **Single Player:**
  - **Tap Anywhere** to Jump.
- **Two Player:**
  - **Tap Left Side**: Agan (P1) Jumps.
  - **Tap Right Side**: Kural (P2) Jumps.
- **Pause**: Tap the "II" button in the top right.

**Ready to build!** 🚀
