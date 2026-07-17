document.addEventListener('DOMContentLoaded', () => {
    console.log('Django e Javascript integrados com sucesso!!')

    const botaoAlerta = document.getElementById('btn-alerta')
    if (botaoAlerta){
        botaoAlerta.addEventListener('click', () => {
            alert('Olá! O JavaScript no Django está funcionando!')
        })
    }

    const botaoCliente = document.getElementById('id-cliente')
    if (botaoCliente){
        botaoCliente.addEventListener('click', () => {
            alert('Este botão é do cliente')
        })
    }
})