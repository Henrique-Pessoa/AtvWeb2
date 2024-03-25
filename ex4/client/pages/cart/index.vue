<script setup lang="ts">
import { ref, onMounted} from "vue";

interface WishlistItem {
  id:number;
  name: string;
  price: number;
  image: string;
  quantity: number;
}

const wishlist = ref<WishlistItem[]>([]);
const total = ref<number>(0);

onMounted(() => {
  const storedWishlist = localStorage.getItem("wishlist");
  if (storedWishlist) {
    wishlist.value = JSON.parse(storedWishlist);
  }
  wishlist.value = removeDuplicates(wishlist.value);
  updateTotal();
});

function removeDuplicates(items: WishlistItem[]): WishlistItem[] {
  return items.filter(
    (item, index, self) => index === self.findIndex((t) => t.name === item.name)
  );
}

function updateTotal() {
  total.value = wishlist.value.reduce(
    (acc, item) => acc + item.price * item.quantity,
    0
  );
  updateLocalStorage();
}

function updateQuantity(item: WishlistItem, newQuantity: number) {
  const itemIndex = wishlist.value.findIndex((i) => i.name === item.name);
  if (itemIndex !== -1) {
    wishlist.value[itemIndex].quantity = newQuantity;
    updateTotal();
  }
}

function updateLocalStorage() {
  localStorage.setItem("wishlist", JSON.stringify(wishlist.value));
}

function deleteItem(index: number) {
  wishlist.value.splice(index, 1);
  updateTotal();
}

async function endShop() {
  alert("Compra finalizada");
  console.log("ok")
}


</script>

<template>
  <div class="w-full h-full min-h-screen bg-zinc-800">
    <nav class="w-full bg-zinc-700 h-16 flex items-center justify-between">
  <div>
    <NuxtLink to="/">
      <button class="bg-zinc-100 font-semibold text-black w-24 h-10 rounded-3xl mr-5">
        Home
      </button>
    </NuxtLink>
  </div>
  <div>
    <button class="bg-zinc-100 font-semibold text-black w-24 h-10 rounded-3xl mr-5" @click="endShop()">
      Finalizar
    </button>
  </div>
</nav>
    <div class="flex gap-5 ml-5 flex-wrap flex-col items-center">
      <div
        class="bg-violet-100 border-2 border-violet-400 flex flex-col justify-center items-center gap-5 w-96 h-60 rounded-xl mt-5"
        v-for="(item, index) in wishlist"
        :key="index"
      >
        <h2 class="font-bold">{{ item.name }}</h2>
        <img :src="item.image" class="w-20" />
        <h2>R${{ item.price }}</h2>
        <div class="flex gap-2">
          <h2 class="font-semibold">Quantidade:</h2>
          <input
            class="w-7 h-5 mt-1 bg-violet-300 rounded-md font-mono"
            type="number"
            v-model="item.quantity"
            min="1"
            @change="updateQuantity(item, item.quantity)"
          />
          <button
            @click="deleteItem(index)"
            class="w-16 h-7 rounded-full border-2 border-black"
          >
            Deletar
          </button>
        </div>
      </div>
    </div>
    <div class="w-full h-10 bg-violet-100  mt-5 border-t-2 border-b-2 border-purple-600 text-center">
      <h1 class="font-bold text-2xl">Valor total a ser pago: R${{ total.toFixed(2) }}</h1>
    </div>
  </div>
</template>
