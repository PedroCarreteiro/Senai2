<script setup>
defineProps({
  mensagem: {
    type: String,
    required: true,
  },
})
</script>

<template>
    <div class="div">
        <h1>{{ mensagem }}</h1>
    </div>
</template>

<style scoped>

h1{
    font-size: 5rem;
    color: with;
}

.div{
    display: flex;
    flex-direction: row;
    align-items: center;
    border: 2px solid red;
}

</style>
