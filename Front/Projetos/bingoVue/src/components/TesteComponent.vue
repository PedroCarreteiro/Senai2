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
    font-size: 10rem;
    color: with;
}

.div{
    display: flex;
    flex-direction: line;
    align-items: center;
}

</style>
