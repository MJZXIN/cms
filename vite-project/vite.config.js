import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver} from 'unplugin-vue-components/resolvers'
import { viteMockServe } from 'vite-plugin-mock'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    viteMockServe({
      mockPath: './src/mock',
      localEnabled: process.env.USE_MOCK || false,
      prodEnable: process.env.USER_CHUNK_MOCK || false,
      logger: process.env.MOCK_LOG || false
    }),
    AutoImport({
      imports: ['vue'] ,
      resolvers: [ElementPlusResolver()],
      dts: './auto-import.d.ts',
      eslintrc: {
        enabled: false
      }
    }),
    Components({
      resolvers: [ElementPlusResolver()]
    })
  ],
})
