<template>
    <form id="fruits">
        <label>{{ t('select') }}</label>
        <select v-model.number="select">
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select>
    </form>
    <p>{{ t('fruits.banana') }}</p>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'
const { t } = useI18n({ useScope: 'global' })
const select = ref(0)
</script>

<i18n lang="yaml">
    select: Do you want banana?
    fruits:
        banana: 'no bananas | {n} banana | {n} bananas'
</i18n>