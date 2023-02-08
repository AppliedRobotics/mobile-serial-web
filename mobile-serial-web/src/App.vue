<template>
  <div class="flex flex-column mt-5 pt-2 align-items-center border w-7 m-auto">
    <div
      v-for="task in tasks"
      :key="task.id"
      class="mb-2 list-elem"
      @click="selectedId = task.id"
      :class="{
        'list-elem-active': task.id === activeId,
        'list-elem-selected': task.id === selectedId,
      }"
    >
      {{ task.name }}
    </div>
    <Button @click="play" class="mb-2" label="Отправить задачу" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "App",
  data() {
    return {
      activeId: -1,
      selectedId: -1,
      tasks: [],
    };
  },
  mounted() {
    fetch("/api/list", {
      method: "GET",
    })
      .then((data) => {
        data.json().then((text) => {
          this.tasks = text.tasks[0];
        });
      })
      .catch((e) => {
        console.error(e);
      });

    setInterval(() => {
      fetch("/api/get", {
        method: "GET",
      })
        .then((data) => {
          data.json().then((text) => {
            this.activeId = text.id;
          });
        })
        .catch((e) => {
          console.error(e);
        });
    }, 500);
  },
  methods: {
    play() {
      fetch(`/api/set/${this.selectedId}`, {
        method: "GET",
      });
    },
  },
});
</script>

<style>
* {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 1.5rem;
}
.border {
  border: 1px solid gray;
  border-radius: 5px;
}
.list-elem {
  padding: 0.3rem 9rem;
  cursor: pointer;
}
.list-elem:hover {
  background-color: var(--gray-400);
  border-radius: 4px;
}
.list-elem-active {
  background-color: var(--gray-700);
  border-radius: 4px;
}
.list-elem-selected {
  background-color: var(--gray-400);
  border-radius: 4px;
}
</style>
