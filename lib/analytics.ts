type TrackPayload = {
  event: string;
  label?: string;
  value?: string | number;
  href?: string;
  extra?: Record<string, string>;
};

const endpoint = process.env.NEXT_PUBLIC_EVENT_ENDPOINT ?? "";

export const trackEvent = (payload: TrackPayload) => {
  if (!endpoint || typeof window === "undefined") {
    return;
  }

  const body = JSON.stringify({
    ...payload,
    path: window.location.pathname,
    ts: new Date().toISOString()
  });

  if (navigator.sendBeacon) {
    const blob = new Blob([body], { type: "application/json" });
    navigator.sendBeacon(endpoint, blob);
    return;
  }

  fetch(endpoint, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body,
    keepalive: true
  }).catch(() => {});
};
