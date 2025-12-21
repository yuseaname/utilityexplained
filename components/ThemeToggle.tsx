"use client";

import { useEffect, useState } from "react";

const THEME_KEY = "upe-theme";

type Theme = "light" | "dark";

const getPreferredTheme = (): Theme => {
  if (typeof window === "undefined") return "light";
  const stored = window.localStorage.getItem(THEME_KEY) as Theme | null;
  if (stored === "light" || stored === "dark") return stored;
  return window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";
};

const ThemeToggle = () => {
  const [theme, setTheme] = useState<Theme>("light");

  useEffect(() => {
    const preferred = getPreferredTheme();
    setTheme(preferred);
    document.documentElement.dataset.theme = preferred;
  }, []);

  const toggleTheme = () => {
    const next = theme === "light" ? "dark" : "light";
    setTheme(next);
    document.documentElement.dataset.theme = next;
    window.localStorage.setItem(THEME_KEY, next);
  };

  return (
    <button className="theme-toggle" onClick={toggleTheme} type="button">
      <span className="theme-toggle__label">Theme</span>
      <span aria-hidden="true" className="theme-toggle__icon">
        {theme === "light" ? "Sun" : "Moon"}
      </span>
    </button>
  );
};

export default ThemeToggle;
