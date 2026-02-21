# Sensor de Temperatura Distribuído Utilizando Kubernetes e Edge Compunting

Este projeto demonstra na prática conceitos de **Edge Computing aplicados a IoT**, utilizando um **cluster Kubernetes geograficamente distribuído**.

A aplicação simula sensores industriais que enviam dados de temperatura para nós regionais (edge), onde decisões críticas são tomadas localmente antes do envio de dados agregados para a nuvem central.

---

# Objetivo

Demonstrar:

- ✅ Processamento local (Edge)
- ✅ Baixa latência para decisões críticas
- ✅ Redução de tráfego para a nuvem
- ✅ Resiliência quando o Cloud está indisponível
- ✅ Distribuição real de workloads usando NodeSelector

---

# Arquitetura

       ┌──────────────────┐
       │  Sensor Nordeste │
       └────────┬─────────┘
                ↓
       ┌──────────────────┐
       │ Edge Nordeste    │  (ids-rn)
       └────────┬─────────┘
                │
                │ Dados agregados
                ↓
           ┌───────────┐
           │   Cloud   │  (vm1-ac)
           └───────────┘
                ↑
                │
       ┌────────┴─────────┐
       │ Edge Sudeste     │  (ids-rj)
       └────────┬─────────┘
                ↓
       ┌──────────────────┐
       │ Sensor Sudeste   │
       └──────────────────┘

---

# Componentes

## Sensor (IoT Simulator)

- Envia temperatura a cada 1 segundo
- Comunicação HTTP com o Edge regional
- Simula ambiente industrial

## Edge Processor

- Recebe dados do sensor
- Avalia regra crítica:

if temperature > 80°C:
    gerar alerta imediato
  
- Envia apenas agregações a cada 10 mensagens para o Cloud
- Continua funcionando mesmo se o Cloud estiver offline

## Cloud Aggregator

- Recebe apenas dados agregados
- Centraliza informações das regiões

---

# Infraestrutura Kubernetes

## Nodes utilizados

| Node   | Função |
|--------|--------|
| ids-rn | Edge Nordeste |
| ids-rj | Edge Sudeste |
| ids-go | Cloud Central |

---

## Labels Aplicadas

```bash
kubectl label node ids-rn region=nordeste
kubectl label node ids-rj region=sudeste
kubectl label node ids-go region=cloud

kubectl apply -f k8s/cloud.yaml
kubectl apply -f k8s/edge-nordeste.yaml
kubectl apply -f k8s/sensor-nordeste.yaml
```

## Verificar Dados Coletados pelo Edge
```bash
kubectl logs -f deployment/edge-nordeste
```

## Simular Falha do Cloud
```bash
kubectl scale deployment cloud --replicas=0
```
