<template>
    <div class="app-container">
        <h1>Hello from Vue.js</h1>

        <div style="text-align:center;">
            <p v-show="areWeWaitingForTheAnswer">
                {{secondsLeft}} second(s) left to guess the answer
            </p>
            <h3>Answer on ping is {{theAnswer}}</h3>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'app',

        data() {
            return {
                theAnswer: 'unknown',
                secondsLeft: 10,
            }
        },

        created() {
            console.log('Root element of the application has been created');

            this.waitForTheAnswer();
        },

        methods: {
            waitForTheAnswer() {
                let intervalId = setInterval(() => {
                    this.secondsLeft -= 1;
                }, 1000);

                setTimeout(() => {
                    clearTimeout(intervalId);

                    this.guessTheAnswer();
                }, this.secondsLeft * 1000);
            },

            guessTheAnswer() {
                axios.get('/api/ping').then(response => {
                    this.theAnswer = response.data.data.answer;
                });
            },
        },

        computed: {
            areWeWaitingForTheAnswer() {
                return this.secondsLeft > 0;
            }
        },
    };
</script>

<style>
    h1 {
        text-align: center;
    }
</style>
