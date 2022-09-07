import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";
import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import { ElementPlusResolver } from "unplugin-vue-components/resolvers";
import {
  createStyleImportPlugin,
  ElementPlusResolve,
} from "vite-plugin-style-import";

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
  return {
    server: {
      port: 3000,
    },
    envDir: process.cwd(),
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
    // 打包时不生成.map文件
    productionSourceMap: false,
    plugins: [
      vue(),
      AutoImport({
        resolvers: [ElementPlusResolver()],
      }),
      Components({
        resolvers: [ElementPlusResolver()],
      }),
      createStyleImportPlugin({
        resolves: [ElementPlusResolve()],
        libs: [
          {
            libraryName: "element-plus",
            esModule: true,
            resolveStyle: (name) => {
              return `element-plus/theme-chalk/${name}.css`;
            },
          },
        ],
      }),
    ],
  };
});
