<script lang="ts" setup>
import InputSwitch from 'primevue/inputswitch';
const operation = ref("");
const checked = ref(false);
</script>

<template>
    <main :class="{'bg-neutral-800': checked, 'bg-neutral-300': !checked}" class="w-full min-h-screen flex flex-col items-center overflow-hidden">
      <h1 class="text-4xl mt-5">Calculator</h1>
      <div :class="{'bg-neutral-600': checked, 'bg-neutral-400': !checked}" class="w-[30rem] h-[20rem] flex flex-col flex-wrap justify-center items-center gap-2 mt-5 rounded-2xl relative">
        <label>{{ checked ? 'Dark' : 'Light' }}</label>
        <InputSwitch v-model="checked" class="mb-3"/>
        <Math :operation="operation"/>
        <select v-model="operation" class="w-32 h-9 rounded-xl text-center outline-none absolute ml-36 mt-16 md:mt-16 md:right-auto md:left-1/2 md:transform md:-translate-x-1/2">
          <option value="Addition">Addition</option>
          <option value="Subtraction">Subtraction</option>
          <option value="Multiplication">Multiplication</option>
          <option value="Division">Division</option>
        </select>
      </div>
    </main>
  </template>
  
