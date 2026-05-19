import DisclaimerModal from '@site/src/components/DisclaimerModal';

import type {ReactNode} from 'react';

export default function Root({children}: {children: ReactNode}) {
  return (
    <>
      <DisclaimerModal />
      {children}
    </>
  );
}
