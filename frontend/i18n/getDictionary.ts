import 'server-only';

export type Locale = 'pt' | 'en' | 'es';

export const locales: Locale[] = ['pt', 'en', 'es'];
export const defaultLocale: Locale = 'pt';

const dictionaries = {
  pt: () => import('./pt.json').then((m) => m.default),
  en: () => import('./en.json').then((m) => m.default),
  es: () => import('./es.json').then((m) => m.default),
};

export type Dictionary = Awaited<ReturnType<typeof dictionaries.pt>>;

export async function getDictionary(locale: Locale): Promise<Dictionary> {
  return dictionaries[locale]();
}

export function isValidLocale(locale: string): locale is Locale {
  return locales.includes(locale as Locale);
}
