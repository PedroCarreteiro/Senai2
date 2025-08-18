<script setup>
import TesteComponent from './components/TesteComponent.vue'
</script>

<template>
    <div class="div">
        <TesteComponent mensagem="Hello"/>
    </div>
</template>

<style scoped>

.div{
    display: flex;
    flex-direction: row;
    align-items: center;
}

</style>
