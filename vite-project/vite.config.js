import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from "path";
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver} from 'unplugin-vue-components/resolvers'
import { viteMockServe } from 'vite-plugin-mock'

// https://vitejs.dev/config/
export default ({ mode }) =>{
    // 拿到/env中的环境变量配置
    const env = loadEnv(mode, path.resolve(process.cwd(), "env"))

    return defineConfig({
      server: {
          host: env.VITE_SERVER_HOST || 'localhost',
          port: env.VITE_SERVER_PORT || 3000,
          open: env.VITE_SERVER_OPEN == 'true' || false,
      },
      envDir: path.resolve(process.cwd(), "env"), 
      resolve: {
          alias: {
            "@": path.resolve(process.cwd(), "src"),
            views: path.resolve(process.cwd(), "src/views"),
            utils: path.resolve(process.cwd(), "src/utils"),
            api: path.resolve(process.cwd(), "src/api"),
            components: path.resolve(process.cwd(), "src/components"),
            router: path.resolve(process.cwd(), "src/router"),
            store: path.resolve(process.cwd(), "src/store"),
          },
        },
      plugins: [
          vue(),
          viteMockServe({
            mockPath: './src/mock',
            // 无法关闭
            localEnabled: env.VITE_USE_MOCK == 'true' || false,
            prodEnable: env.VITE_USER_CHUNK_MOCK == 'true' || false,
            injectCode: `
            import { setupProdMockServer } from './mockProdServer';
            setupProdMockServer();
            `,//如果生产环境开启了 mock 功能,即prodEnabled=true.则该代码会被注入到injectFile对应的文件的底部。默认为main.{ts,js}
            logger: env.VITE_MOCK_LOG == 'true' || false
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
        css: {
          preprocessorOptions: {
            // 全局样式引入
            scss: {
              additionalData: '@import "./src/assets/styles/index.scss";',
              javascriptEnabled: true
            }
          }
        }
    })
  }
