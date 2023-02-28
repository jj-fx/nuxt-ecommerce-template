
export const useLogin = () => useState<boolean>('login', () => { return false });

export const useCategories = () => useState<Object>('categories', () => { return {} });
