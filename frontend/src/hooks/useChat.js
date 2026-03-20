import { useState } from 'react'
import { askQuestion, buildIndex } from '../services/api'

export function useChat() {
  const [loading, setLoading] = useState(false)
  const [indexLoading, setIndexLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [messages, setMessages] = useState([])
  const [error, setError] = useState('')

  const handleBuildIndex = async () => {
    try {
      setIndexLoading(true)
      setError('')
      return await buildIndex()
    } finally {
      setIndexLoading(false)
    }
  }

  const handleAsk = async (question) => {
    try {
      setLoading(true)
      setError('')
      const response = await askQuestion(question)
      setResult(response)
      setMessages((prev) => [
        ...prev,
        { role: 'user', content: question },
        { role: 'assistant', content: response.answer }
      ])
      return response
    } catch (err) {
      setError(err.message)
      throw err
    } finally {
      setLoading(false)
    }
  }

  return {
    loading,
    indexLoading,
    result,
    messages,
    error,
    setError,
    handleBuildIndex,
    handleAsk
  }
}
