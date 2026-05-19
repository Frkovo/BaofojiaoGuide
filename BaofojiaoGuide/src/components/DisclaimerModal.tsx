import { useEffect, useState } from 'react';
import clsx from 'clsx';

const STORAGE_KEY = 'baofojiao-disclaimer-accepted';

export default function DisclaimerModal() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const accepted = localStorage.getItem(STORAGE_KEY);
    if (!accepted) {
      setVisible(true);
    }
  }, []);

  const handleAccept = () => {
    localStorage.setItem(STORAGE_KEY, 'true');
    setVisible(false);
  };

  if (!visible) return null;

  return (
    <div className="disclaimer-overlay">
      <div className="disclaimer-modal">
        <h2>免责声明 / Disclaimer</h2>
        <p>
          AI 可能会产生"幻觉"（生成不准确或虚构的内容）。
          本站内容<strong>仅作参考</strong>，请以官方教材和考纲为准。
        </p>
        <p>
          Frk <strong>不对 AI 生成的内容的正确性或完整性负责</strong>。
          使用本站资料所产生的任何后果由使用者自行承担。
        </p>
        <p style={{ fontSize: '0.85em', color: 'var(--ifm-color-emphasis-600)' }}>
          AI may produce hallucinations (inaccurate or fabricated content).
          All materials on this site are for <strong>reference only</strong>.
          Always refer to official textbooks and syllabuses.
          Frk is <strong>not responsible</strong> for the accuracy or completeness
          of AI-generated content.
        </p>
        <button className={clsx('button', 'button--primary')} onClick={handleAccept}>
          我知道了 / I Understand
        </button>
      </div>
    </div>
  );
}
