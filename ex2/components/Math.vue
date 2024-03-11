<script lang="ts" setup>
import { ref, defineProps } from 'vue';

const mathOperation = defineProps({
  operation: String,
});

const value1:Ref<number> = ref(0.0);
const value2:Ref<number> = ref(0.0);

const result = () => {
  if (mathOperation.operation === "Addition") {
    return value1.value + value2.value;
  } else if (mathOperation.operation === "Subtraction") {
    return value1.value - value2.value;
  } else if (mathOperation.operation === "Multiplication") {
    return value1.value * value2.value;
  } else if (mathOperation.operation === "Division") {
    if(value2.value == 0){
      return "Error can't divide for 0"
    }
    return value1.value / value2.value;
  }
};
</script>

<template>
  <div class="flex flex-col gap-2 justify-center content-start">
    <label class="flex flex-col ">Number 1: </label>
    <input v-model="value1" type="number" class="w-40 h-7 outline-none  rounded-lg text-end border-2 border-teal-900  bg-neutral-300"/>
    <label class="flex flex-col ">Number 2: </label>
    <input v-model="value2" type="number" class="w-40 h-7 outline-none  rounded-lg text-end border-2 border-teal-900 bg-neutral-300"/>
    <h1 class=" text-2xl">Result: {{ result() }}</h1>
  </div>
</template>
