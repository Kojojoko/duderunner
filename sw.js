const CACHE_NAME = 'dude-runner-v2';
const ASSETS = [
    './',
    './index.html',
    './manifest.json',
    './assets/icon.png',
    './assets/hero_sheet_normalized.png',
    './assets/bg_sky.png',
    './assets/bg_ground.png',
    './assets/logo.png',
    './audio/Oorum_Blood.wav',
    './audio/jump.mp3'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(ASSETS);
        })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});
