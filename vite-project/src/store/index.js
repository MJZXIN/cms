import { createPinia } from "pinia"
import { usePersist } from "pinia-use-persist"
import { userStore } from "./modules/userStore"

const store = createPinia()
store.use(usePersist)

export default store