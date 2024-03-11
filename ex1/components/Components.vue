<script lang="ts" setup>
import { ref } from 'vue';
const gender = ref("");

</script>

<template>
    <div class="bg-stone-700 h-screen w-screen flex flex-col items-center">
        <h1 class="text-white text-4xl font-bold">Select some gender</h1>
        <select v-model="gender" class="w-40 h-10 mt-10 rounded-xl text-center font-bold text-red-400 outline-none border-2 border-red-300 ">
            <option value="Terror">Terror</option>
            <option value="Comedia">Comedia</option>
            <option value="Ação">Ação</option>
            <option value="Anime">Anime</option>
            <option value="Ficção cientifica">Ficção cientifica</option>
        </select>
        <h5 class="mt-10 font-bold text-2xl text-white"> Você escolheu o genero: {{ gender }}</h5>
    </div>
</template>