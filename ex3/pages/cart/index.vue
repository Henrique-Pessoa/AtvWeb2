<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';

const wishlist:any = ref([]);
const groupedWishlist:any = computed(() => {
  const groupedItems:any = {};
  wishlist.value.forEach((item:any) => {
    if (!groupedItems[item.name]) {
      groupedItems[item.name] = { ...item, quantity: 1 };
    } else {
      groupedItems[item.name].quantity++;
    }
  });
  return Object.values(groupedItems);
});

onMounted(() => {
  const storedWishlist = localStorage.getItem('wishlist');
  if (storedWishlist) {
    wishlist.value = JSON.parse(storedWishlist);
  }
});
</script>

<template>
  <div>
    <h1>Carrinho</h1>
    <ul>
      <li v-for="item in groupedWishlist" :key="item.name">
        <div>
          Nome: {{ item.name }}
        </div>
        <div>
          Preço: {{ item.price }}
        </div>
        <div>
          Quantidade: {{ item.quantity }}
        </div>
      </li>
    </ul>
  </div>
</template>
