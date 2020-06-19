/* Punjabi locals for flatpickr */
import { CustomLocale } from "types/locale";
import { FlatpickrFn } from "types/instance";

const fp: FlatpickrFn =
  typeof window !== "undefined" && window.flatpickr !== undefined
    ? window.flatpickr
    : {
        l10ns: {},
      } as FlatpickrFn;

export const Punjabi: CustomLocale = {
  weekdays: {
    shorthand: ["ਐਤ", "ਸੋਮ", "ਮੰਗਲ", "ਬੁੱਧ", "ਵੀਰ", "ਸ਼ੁੱਕਰ", "ਸ਼ਨਿੱਚਰ"],
    longhand: [
      "ਐਤਵਾਰ",
      "ਸੋਮਵਾਰ",
      "ਮੰਗਲਵਾਰ",
      "ਬੁੱਧਵਾਰ",
      "ਵੀਰਵਾਰ",
      "ਸ਼ੁੱਕਰਵਾਰ",
      "ਸ਼ਨਿੱਚਰਵਾਰ",
    ],
  },

  months: {
    shorthand: [
      "ਜਨ",
      "ਫ਼ਰ",
      "ਮਾਰ",
      "ਅਪ੍ਰੈ",
      "ਮਈ",
      "ਜੂਨ",
      "ਜੁਲਾ",
      "ਅਗ",
      "ਸਤੰ",
      "ਅਕ",
      "ਨਵੰ",
      "ਦਸੰ",
    ],
    longhand: [
      "ਜਨਵਰੀ",
      "ਫ਼ਰਵਰੀ",
      "ਮਾਰਚ",
      "ਅਪ੍ਰੈਲ",
      "ਮਈ",
      "ਜੂਨ",
      "ਜੁਲਾਈ",
      "ਅਗਸਤ",
      "ਸਤੰਬਰ",
      "ਅਕਤੂਬਰ",
      "ਨਵੰਬਰ",
      "ਦਸੰਬਰ",
    ],
  },
};

fp.l10ns.pa = Punjabi;

export default fp.l10ns;
