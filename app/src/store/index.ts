import type { App } from "vue";
import { createPinia } from "pinia";
import { usePersist } from "pinia-use-persist";

const store = createPinia();
store.use(usePersist);

// export function setupStore(app: App<Element>) {
//   app.use(store);
// }

export default store;
