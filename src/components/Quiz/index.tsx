import React, { useState } from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

export interface Question {
  question: string;
  options: string[];
  correctAnswerIndex: number;
  justification: string;
}

export interface QuizProps {
  questions: Question[];
}

export default function Quiz({ questions }: QuizProps): JSX.Element {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [score, setScore] = useState(0);
  const [showResults, setShowResults] = useState(false);

  const handleOptionClick = (index: number) => {
    if (isSubmitted) return;
    setSelectedAnswer(index);
  };

  const handleSubmit = () => {
    if (selectedAnswer === null) return;
    setIsSubmitted(true);

    if (selectedAnswer === questions[currentQuestion].correctAnswerIndex) {
      setScore(score + 1);
    }
  };

  const handleNext = () => {
    if (currentQuestion + 1 < questions.length) {
      setCurrentQuestion(currentQuestion + 1);
      setSelectedAnswer(null);
      setIsSubmitted(false);
    } else {
      setShowResults(true);
    }
  };

  const resetQuiz = () => {
    setCurrentQuestion(0);
    setSelectedAnswer(null);
    setIsSubmitted(false);
    setScore(0);
    setShowResults(false);
  };

  if (showResults) {
    return (
      <div className={clsx('card shadow--lw', styles.quizContainer)}>
        <div className="card__header">
          <h3>Resultados del Test</h3>
        </div>
        <div className="card__body">
          <p className={styles.scoreText}>
            Has acertado {score} de {questions.length} preguntas ({(score / questions.length * 100).toFixed(0)}%).
          </p>
          <div className="margin-top--md">
            <button className="button button--primary" onClick={resetQuiz}>Reintentar Test</button>
          </div>
        </div>
      </div>
    );
  }

  const q = questions[currentQuestion];

  return (
    <div className={clsx('card shadow--lw', styles.quizContainer)}>
      <div className="card__header">
        <div className={styles.progressText}>Pregunta {currentQuestion + 1} de {questions.length}</div>
        <h4 dangerouslySetInnerHTML={{ __html: q.question }} />
      </div>
      <div className="card__body">
        <ul className={styles.optionsList}>
          {q.options.map((option, index) => {
            let itemClass = styles.optionItem;

            if (isSubmitted) {
              if (index === q.correctAnswerIndex) {
                itemClass = clsx(itemClass, styles.optionCorrect);
              } else if (index === selectedAnswer && selectedAnswer !== q.correctAnswerIndex) {
                itemClass = clsx(itemClass, styles.optionIncorrect);
              } else {
                itemClass = clsx(itemClass, styles.optionDisabled);
              }
            } else if (index === selectedAnswer) {
              itemClass = clsx(itemClass, styles.optionSelected);
            }

            return (
              <li
                key={index}
                className={itemClass}
                onClick={() => handleOptionClick(index)}
                dangerouslySetInnerHTML={{ __html: option }}
              />
            );
          })}
        </ul>

        {isSubmitted && (
          <div className={clsx('alert margin-top--md', selectedAnswer === q.correctAnswerIndex ? 'alert--success' : 'alert--danger')}>
            <strong>{selectedAnswer === q.correctAnswerIndex ? '¡Correcto!' : 'Incorrecto.'}</strong>
            <div className="margin-top--sm" dangerouslySetInnerHTML={{ __html: q.justification }} />
          </div>
        )}
      </div>
      <div className="card__footer">
        {!isSubmitted ? (
          <button
            className="button button--primary"
            onClick={handleSubmit}
            disabled={selectedAnswer === null}
          >
            Comprobar
          </button>
        ) : (
          <button
            className="button button--primary"
            onClick={handleNext}
          >
            {currentQuestion + 1 === questions.length ? 'Ver Resultados Finales' : 'Siguiente Pregunta'}
          </button>
        )}
      </div>
    </div>
  );
}
