/* eslint-disable vue/multi-word-component-names */
import { createApp } from "vue";
import App from "./App.vue";

import PrimeVue from "primevue/config";
import "primevue/resources/themes/bootstrap4-dark-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";
import "primeflex/primeflex.css";

import Button from "primevue/button";

const app = createApp(App).use(PrimeVue, { ripple: true });

app.component("Button", Button);

app.mount("#app");
