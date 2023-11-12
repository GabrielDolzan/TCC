<template>
    <div class="p-3" style="display: flex; height: 53rem;">
        <div class="cards rounded p-3" style="width: 20rem; min-width: 15rem;">
            <DashboardSidebar @dashboard="exibirDashboard" @salvar="salvarDashboard" @error="error" @alerta="alerta" />
        </div>
        <Chart class="ms-3 rounded cards" :info="dados" :key="chartKey" v-if="dados" />
    </div>

    <div class="toast-container position-fixed bottom-0 start-50 translate-middle-x p-3">
        <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="toast-header">
                <strong class="me-auto">{{ this.tituloToast }}</strong>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Fechar"></button>
            </div>
            <div class="toast-body text-black">
                {{ this.msgToast }}
            </div>
        </div>
    </div>

    <div class="modal fade" id="modal" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content cards">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="modalLabel">Salvar Dashboard</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form>
                        <div class="mb-3">
                            <label for="nome" class="form-label">Nome:</label>
                            <input type="text" class="form-control" id="nome" v-model="nome" required />
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fechar</button>
                    <button type="button" class="btn btn-primary" @click="salvarDashboardModal">Confirmar</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import DashboardSidebar from '@/components/DashboardSidebar.vue'
import Chart from '@/components/Chart.vue';
import axios from 'axios'

export default {
    components: {
        DashboardSidebar,
        Chart
    },
    data() {
        return {
            dados: null,
            chartKey: 0,
            tituloToast: '',
            msgToast: '',
            nome: '',
            jogo: '',
            info: ''
        }
    },
    methods: {
        exibirDashboard(dados) {
            this.dados = dados.data;
            if (this.dados.error) {
                const toastLiveExample = document.getElementById('liveToast')
                const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)

                this.tituloToast = 'Erro'
                this.msgToast = this.dados.error

                toastBootstrap.show()
            } else if (this.dados) {
                this.chartKey++;
            }
        },
        error() {
            const toastLiveExample = document.getElementById('liveToast')
            const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)

            this.tituloToast = 'Erro'
            this.msgToast = 'Erro ao gerar dashboard.'

            toastBootstrap.show()
        },
        alerta(titulo, mensagem) {
            const toastLiveExample = document.getElementById('liveToast')
            const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)

            this.tituloToast = titulo
            this.msgToast = mensagem

            toastBootstrap.show()
        },
        salvarDashboard(jogo, informacoes) {
            this.jogo = jogo
            this.info = informacoes

            const modal = document.getElementById('modal')
            const modalBootstrap = bootstrap.Modal.getOrCreateInstance(modal)

            modalBootstrap.show()
        },
        salvarDashboardModal() {
            if (this.nome) {
                const modal = document.getElementById('modal')
                const modalBootstrap = bootstrap.Modal.getOrCreateInstance(modal)

                try {
                    axios.post('/api/dashboard/', {
                        game: this.jogo,
                        nome: this.nome,
                        info: this.info
                    }).then(response => {
                        this.alerta('Sucesso', 'Dashboard salvo com sucesso.')
                        this.nome = ''
                        modalBootstrap.hide()
                    }).catch(error => {
                        this.alerta('Erro', 'Erro ao salvar o dashboard.')
                    })
                } catch (error) {
                    this.alerta('Erro', 'Erro ao salvar o dashboard.')
                }
            } else {
                this.alerta('Atenção', 'Preencha os campos obrigatórios para salvar.')
            }
        }
    },
    mounted() {
    }
};

</script>