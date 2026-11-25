/**
 * DKSchV Schweiz · Wetter-adaptives Weihnachts-Special
 * Passt das Weihnachts-Layout dynamisch an das aktuelle Tageswetter in Naters/Wallis an.
 */
(function() {
  'use strict';

  const WEATHER_CACHE_KEY = 'dkschv_weather_cache';
  const CACHE_TTL_MS = 15 * 60 * 1000; // 15 Minuten

  // WMO Wettercodes Mapping auf lesbare Texte & Icons
  function decodeWmo(code, temp) {
    if ([71, 73, 75, 77, 85, 86].includes(code) || temp <= 0) {
      return { type: 'snow', label: 'Schneefall / Frost', icon: '❄️', theme: 'winter-snow' };
    }
    if ([0, 1].includes(code)) {
      return { type: 'clear', label: 'Klar & Sonnig', icon: '☀️', theme: 'winter-sun' };
    }
    if (code === 2) {
      return { type: 'partly_cloudy', label: 'Leicht bewölkt', icon: '⛅', theme: 'winter-sun' };
    }
    if ([45, 48].includes(code)) {
      return { type: 'fog', label: 'Mystischer Winternebel', icon: '🌫️', theme: 'cozy-fireplace' };
    }
    if ([51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82].includes(code)) {
      return { type: 'rain', label: 'Winterregen / Schauer', icon: '🌧️', theme: 'cozy-fireplace' };
    }
    return { type: 'cloudy', label: 'Bewölkt', icon: '☁️', theme: 'cozy-fireplace' };
  }

  async function fetchNatersWeather() {
    try {
      const cached = sessionStorage.getItem(WEATHER_CACHE_KEY);
      if (cached) {
        const parsed = JSON.parse(cached);
        if (Date.now() - parsed.timestamp < CACHE_TTL_MS) {
          return parsed.data;
        }
      }

      // Naters / Wallis (Lat 46.33, Lon 7.99)
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 3500);

      const resp = await fetch(
        'https://api.open-meteo.com/v1/forecast?latitude=46.33&longitude=7.99&current=temperature_2m,weather_code,is_day&timezone=Europe%2FZurich',
        { signal: controller.signal }
      );
      clearTimeout(timeoutId);

      if (!resp.ok) throw new Error('Weather API status ' + resp.status);
      const json = await resp.json();
      const current = json.current || {};
      const data = {
        temp: Math.round(current.temperature_2m ?? 2),
        code: current.weather_code ?? 0,
        isDay: current.is_day ?? 1
      };

      sessionStorage.setItem(WEATHER_CACHE_KEY, JSON.stringify({
        timestamp: Date.now(),
        data: data
      }));
      return data;
    } catch (e) {
      console.warn('Wetterabfrage fehlgeschlagen, nutze saisonalen Winter-Standard:', e);
      return { temp: 0, code: 71, isDay: 1 }; // Sanfter Winter-Fallback
    }
  }

  function applyWeatherTheme(weather) {
    const wInfo = decodeWmo(weather.code, weather.temp);
    const banners = document.querySelectorAll('.xmas-weather-banner');
    if (!banners.length) return;

    banners.forEach(banner => {
      // 1. Wetter-Pill Badge aktualisieren
      const pill = banner.querySelector('.xmas-weather-pill');
      if (pill) {
        pill.innerHTML = `📍 Naters / Wallis: <strong>${weather.temp}°C</strong> · ${wInfo.label} ${wInfo.icon}`;
      }

      // 2. Dynamische Headline & Text basierend auf Wetter
      const headline = banner.querySelector('.xmas-dynamic-headline');
      const subtext = banner.querySelector('.xmas-dynamic-subtext');

      if (wInfo.type === 'snow') {
        banner.style.background = 'radial-gradient(ellipse at 80% 20%, #1e293b 0%, #0f172a 40%, #7f1d1d 100%)';
        banner.style.borderColor = 'rgba(56, 189, 248, 0.5)';
        banner.style.boxShadow = '0 12px 30px -5px rgba(56, 189, 248, 0.2), 0 0 20px rgba(220, 38, 38, 0.2)';
        if (headline) headline.textContent = '❄️ 50 % Weihnachts-Rabatt: Schneewetter für Ihre massgeschneiderte App!';
        if (subtext) subtext.textContent = 'Draussen rieselt der Schnee in den Schweizer Alpen – drinnen planen wir Ihre Wunsch-App für iOS & Android zum exklusiven halben Festpreis.';
        addSnowflakes(banner);
      } else if (wInfo.type === 'clear' || wInfo.type === 'partly_cloudy') {
        banner.style.background = 'linear-gradient(135deg, #0f172a 0%, #1e1b4b 40%, #991b1b 100%)';
        banner.style.borderColor = 'rgba(245, 158, 11, 0.45)';
        banner.style.boxShadow = '0 12px 30px -5px rgba(245, 158, 11, 0.2), 0 0 20px rgba(220, 38, 38, 0.25)';
        if (headline) headline.textContent = '☀️ 50 % Weihnachts-Rabatt: Mit klarem Kopf & 50 % ins neue App-Jahr!';
        if (subtext) subtext.textContent = 'Klares Winterwetter, glasklare Festpreise: Starten Sie Ihr digitales Projekt ohne Stundensatz-Risiko und sichern Sie sich 50 % Weihnachtsbonus.';
        addSnowflakes(banner, 8); // Dezent
      } else {
        // Gemütliches Kaminfeuer / Chalet-Wetter (Regen, Wolken, Nebel)
        banner.style.background = 'linear-gradient(135deg, #18181b 0%, #27272a 40%, #7f1d1d 100%)';
        banner.style.borderColor = 'rgba(239, 68, 68, 0.45)';
        banner.style.boxShadow = '0 12px 30px -5px rgba(220, 38, 38, 0.25)';
        if (headline) headline.textContent = '🔥 50 % Weihnachts-Rabatt: Gemütlich digitalisieren statt frieren!';
        if (subtext) subtext.textContent = 'Ungemütlich draussen? Perfekte Zeit, um lästigen Papierkram abzuschaffen: Wir programmieren Ihre 100 % massgeschneiderte Business-App zum halben Preis.';
        addSnowflakes(banner, 10);
      }
    });
  }

  // Sanfte, ressourcenschonende Schneeflocken-Animation im Banner
  function addSnowflakes(container, count = 16) {
    if (container.querySelector('.xmas-snow-canvas')) return;

    const wrapper = document.createElement('div');
    wrapper.className = 'xmas-snow-canvas';
    wrapper.style.position = 'absolute';
    wrapper.style.top = '0';
    wrapper.style.left = '0';
    wrapper.style.width = '100%';
    wrapper.style.height = '100%';
    wrapper.style.overflow = 'hidden';
    wrapper.style.pointerEvents = 'none';
    wrapper.style.zIndex = '1';

    container.style.position = 'relative';

    for (let i = 0; i < count; i++) {
      const flake = document.createElement('span');
      flake.textContent = ['❄', '❅', '•', '❆'][Math.floor(Math.random() * 4)];
      flake.style.position = 'absolute';
      flake.style.color = 'rgba(255, 255, 255, ' + (0.3 + Math.random() * 0.5) + ')';
      flake.style.fontSize = (10 + Math.random() * 14) + 'px';
      flake.style.left = Math.random() * 100 + '%';
      flake.style.top = '-20px';
      flake.style.animation = `xmasSnowFall ${4 + Math.random() * 6}s linear infinite`;
      flake.style.animationDelay = (Math.random() * 5) + 's';
      wrapper.appendChild(flake);
    }

    container.prepend(wrapper);
  }

  // CSS Keyframes injizieren falls noch nicht vorhanden
  function injectSnowKeyframes() {
    if (document.getElementById('xmas-snow-style')) return;
    const style = document.createElement('style');
    style.id = 'xmas-snow-style';
    style.textContent = `
      @keyframes xmasSnowFall {
        0% { transform: translateY(0) rotate(0deg); opacity: 0; }
        20% { opacity: 0.8; }
        80% { opacity: 0.8; }
        100% { transform: translateY(160px) rotate(360deg); opacity: 0; }
      }
    `;
    document.head.appendChild(style);
  }

  // Initialisieren
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      injectSnowKeyframes();
      fetchNatersWeather().then(applyWeatherTheme);
    });
  } else {
    injectSnowKeyframes();
    fetchNatersWeather().then(applyWeatherTheme);
  }
})();
